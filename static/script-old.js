const chatBox = document.getElementById("chat-box")

function addMessage(message,sender){

    const msg=document.createElement("div")

    if(sender==="user"){
        msg.className="user-message"
        msg.innerText=message
    }else{
        msg.className="bot-message"
        msg.innerText=message
    }

    chatBox.appendChild(msg)

    chatBox.scrollTop=chatBox.scrollHeight

    return msg
}

function showTyping(){

    const typing=document.createElement("div")
    typing.className="bot-message"

    typing.innerHTML=`
    <div class="typing">
        <span></span>
        <span></span>
        <span></span>
    </div>
    `

    chatBox.appendChild(typing)

    chatBox.scrollTop=chatBox.scrollHeight

    return typing
}

async function sendMessage(){

    const input=document.getElementById("user-input")
    const message=input.value.trim()

    if(message==="") return

    addMessage(message,"user")

    input.value=""

    const typing=showTyping()

    const response=await fetch("/chat",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({message:message})
    })

    const data=await response.json()

    typing.remove()

    addMessage(data.response,"bot")
}

function clearChat(){
    chatBox.innerHTML=""
}