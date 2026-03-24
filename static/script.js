// Modern JavaScript with ES6+ features
class ChatApp {
    constructor() {
        this.chatBox = document.getElementById("chat-box");
        this.userInput = document.getElementById("user-input");
        this.sendBtn = document.getElementById("send-btn");
        this.historySidebar = document.getElementById("history-sidebar");
        this.historyList = document.getElementById("history-list");
        this.charCount = document.getElementById("char-count");
        this.toastContainer = document.getElementById("toast-container");
        
        this.currentPage = 1;
        this.totalPages = 1;
        this.isLoading = false;
        
        this.init();
    }
    
    init() {
        // Event listeners
        this.userInput.addEventListener('input', () => this.updateCharCount());
        this.sendBtn.addEventListener('click', () => this.sendMessage());
        
        // Page close detection for automatic logout
        window.addEventListener('beforeunload', (event) => this.handlePageClose(event));
        window.addEventListener('unload', (event) => this.handlePageClose(event));
        
        // Load initial history
        this.loadHistory();
        
        // Focus input
        this.userInput.focus();
        
        // Clear welcome message when user starts typing
        this.userInput.addEventListener('focus', () => {
            const welcomeMsg = this.chatBox.querySelector('.welcome-message');
            if (welcomeMsg) {
                welcomeMsg.style.opacity = '0.7';
            }
        });
    }
    
    handlePageClose(event) {
        // Send logout request when page is closing
        // Use navigator.sendBeacon for reliable delivery during page unload
        const logoutData = new FormData();
        logoutData.append('logout', 'true');
        
        try {
            navigator.sendBeacon('/logout', logoutData);
        } catch (e) {
            // Fallback for older browsers
            fetch('/logout', {
                method: 'POST',
                body: logoutData,
                keepalive: true
            });
        }
    }
    
    updateCharCount() {
        const length = this.userInput.value.length;
        this.charCount.textContent = length;
        
        if (length > 900) {
            this.charCount.style.color = 'var(--warning-color)';
        } else if (length > 950) {
            this.charCount.style.color = 'var(--error-color)';
        } else {
            this.charCount.style.color = 'var(--text-secondary)';
        }
    }
    
    addMessage(message, sender, isTyping = false) {
        // Remove welcome message on first user message
        const welcomeMsg = this.chatBox.querySelector('.welcome-message');
        if (welcomeMsg && sender === 'user') {
            welcomeMsg.remove();
        }
        
        const msg = document.createElement("div");
        msg.className = `${sender}-message`;
        
        if (isTyping) {
            msg.innerHTML = `
                <div class="typing">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
            `;
        } else {
            msg.textContent = message;
        }
        
        this.chatBox.appendChild(msg);
        this.scrollToBottom();
        
        return msg;
    }
    
    showTyping() {
        return this.addMessage("", "bot", true);
    }
    
    async sendMessage() {
        const message = this.userInput.value.trim();
        
        if (message === "" || this.isLoading) return;
        
        // Clear input and reset char count
        this.userInput.value = "";
        this.updateCharCount();
        
        // Add user message
        this.addMessage(message, "user");
        
        // Show typing indicator
        const typing = this.showTyping();
        
        // Disable input during loading
        this.setLoadingState(true);
        
        try {
            const response = await fetch("/chat", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ message: message })
            });
            
            // Check response status FIRST
            if (!response.ok) {
                let errorData;
                try {
                    errorData = await response.json();
                } catch (e) {
                    errorData = { error: `HTTP ${response.status}: ${response.statusText}` };
                }
                throw new Error(errorData.error || `Server error: ${response.status}`);
            }
            
            // Parse JSON data
            const data = await response.json();
            
            // Remove typing indicator
            typing.remove();
            
            // Add bot response
            this.addMessage(data.response, "bot");
            
            // Refresh history
            this.loadHistory();
            
        } catch (error) {
            console.error('Chat error:', error);
            typing.remove();
            
            const errorMsg = error.message.toLowerCase();
            
            if (errorMsg.includes('429') || errorMsg.includes('rate limit')) {
                this.addMessage("⚠️ Rate limit exceeded. Please wait a moment before trying again.", "bot");
                this.showToast('Rate limit exceeded. Please wait.', 'warning');
            } else if (errorMsg.includes('quota') || errorMsg.includes('exceeded')) {
                this.addMessage("⚠️ API quota exceeded. Please check your API key configuration.", "bot");
                this.showToast('API quota exceeded', 'error');
            } else if (errorMsg.includes('401') || errorMsg.includes('unauthorized')) {
                this.addMessage("⚠️ Authentication error. Please login again.", "bot");
                this.showToast('Please login again', 'error');
            } else {
                this.addMessage("Sorry, I'm having trouble connecting right now. Please try again!", "bot");
                this.showToast('Connection error', 'error');
            }
        } finally {
            this.setLoadingState(false);
            this.userInput.focus();
        }
    }
    
    setLoadingState(loading) {
        this.isLoading = loading;
        this.userInput.disabled = loading;
        this.sendBtn.disabled = loading;
        
        if (loading) {
            this.sendBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';
        } else {
            this.sendBtn.innerHTML = '<i class="fas fa-paper-plane"></i>';
        }
    }
    
    clearChat() {
        if (confirm('Are you sure you want to clear the chat? This cannot be undone.')) {
            this.chatBox.innerHTML = `
                <div class="welcome-message">
                    <i class="fas fa-robot"></i>
                    <h2>Chat Cleared!</h2>
                    <p>Ready for a fresh conversation. What would you like to work on?</p>
                </div>
            `;
            this.showToast('Chat cleared successfully', 'success');
            this.userInput.focus();
        }
    }
    
    async loadHistory(page = 1) {
        try {
            const response = await fetch(`/history?page=${page}`);
            const data = await response.json();
            
            if (!response.ok) {
                throw new Error(data.error || 'Failed to load history');
            }
            
            this.renderHistory(data.chats);
            this.updatePagination(data.pagination);
            
        } catch (error) {
            console.error('History error:', error);
            this.historyList.innerHTML = '<div class="loading">Failed to load history</div>';
        }
    }
    
    renderHistory(chats) {
        if (!chats || chats.length === 0) {
            this.historyList.innerHTML = '<div class="loading">No chat history found</div>';
            return;
        }
        
        this.historyList.innerHTML = chats.map((chat, index) => `
            <div class="history-item" onclick="app.loadChatToInput('${this.escapeHtml(chat.user)}')">
                <div class="user-msg">${this.escapeHtml(chat.user)}</div>
                <div class="bot-msg">${this.escapeHtml(chat.bot)}</div>
                <div class="time">${this.formatTime(chat.time)}</div>
            </div>
        `).join('');
    }
    
    updatePagination(pagination) {
        this.currentPage = pagination.page;
        this.totalPages = pagination.pages;
        
        document.getElementById('page-info').textContent = `Page ${this.currentPage} of ${this.totalPages}`;
        document.getElementById('prev-page').disabled = this.currentPage <= 1;
        document.getElementById('next-page').disabled = this.currentPage >= this.totalPages;
    }
    
    loadChatToInput(message) {
        this.userInput.value = message;
        this.updateCharCount();
        this.userInput.focus();
        this.toggleHistory(); // Close sidebar
    }
    
    loadHistoryPage(direction) {
        const newPage = this.currentPage + direction;
        if (newPage >= 1 && newPage <= this.totalPages) {
            this.loadHistory(newPage);
        }
    }
    
    toggleHistory() {
        this.historySidebar.classList.toggle('hidden');
        if (!this.historySidebar.classList.contains('hidden')) {
            this.loadHistory();
        }
    }
    
    showToast(message, type = 'info') {
        const toast = document.createElement('div');
        toast.className = `toast ${type}`;
        toast.textContent = message;
        
        this.toastContainer.appendChild(toast);
        
        setTimeout(() => {
            toast.style.opacity = '0';
            setTimeout(() => toast.remove(), 300);
        }, 3000);
    }
    
    scrollToBottom() {
        this.chatBox.scrollTop = this.chatBox.scrollHeight;
    }
    
    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }
    
    formatTime(timestamp) {
        try {
            const date = new Date(timestamp);
            const now = new Date();
            const diffMs = now - date;
            const diffMins = Math.floor(diffMs / 60000);
            const diffHours = Math.floor(diffMs / 3600000);
            const diffDays = Math.floor(diffMs / 86400000);
            
            if (diffMins < 1) return 'Just now';
            if (diffMins < 60) return `${diffMins}m ago`;
            if (diffHours < 24) return `${diffHours}h ago`;
            if (diffDays < 7) return `${diffDays}d ago`;
            
            return date.toLocaleDateString();
        } catch {
            return 'Unknown time';
        }
    }
}

// Global functions for HTML onclick handlers
let app;

function handleKeyPress(event) {
    if (event.key === 'Enter' && !event.shiftKey) {
        event.preventDefault();
        app.sendMessage();
    }
}

function sendMessage() {
    app.sendMessage();
}

function clearChat() {
    app.clearChat();
}

function toggleHistory() {
    app.toggleHistory();
}

function loadHistoryPage(direction) {
    app.loadHistoryPage(direction);
}

// Initialize app when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    app = new ChatApp();
    
    // Add keyboard shortcuts
    document.addEventListener('keydown', (e) => {
        // Ctrl/Cmd + H to toggle history
        if ((e.ctrlKey || e.metaKey) && e.key === 'h') {
            e.preventDefault();
            toggleHistory();
        }
        
        // Escape to close history sidebar
        if (e.key === 'Escape' && !app.historySidebar.classList.contains('hidden')) {
            toggleHistory();
        }
    });
    
    // Add some initial polish
    console.log('🤖 AI Growth Companion loaded successfully!');
});
