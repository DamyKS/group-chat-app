<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="upgrade-insecure-requests">
<style>
.chat-input-container {
  display: flex;
  align-items: center;
  border: 1px solid #4c0ae6;
  border-radius: 4px;
  padding: 10px;
  margin-bottom: 10px;
}

#message-input {
  flex: 1;
  border: none;
  outline: none;
  font-size: 16px;
  padding: 5px;
  height: 40px;  /* Initial height */
  min-height: 30px;  /* Set minimum height */
  overflow: hidden;  /* Remove scrollbar */
}

#send-message-button {
  background-color: #4752f7;
  color: #ffff;
  border: none;
  padding: 5px 10px;
  border-radius: 4px;
  cursor: pointer;
}

#send-message-button:hover {
  background-color: #444;
}

body {
  margin: 0 auto;
  max-width: 800px;
  padding: 0 20px;
}

.container {
  border: 2px solid #eff6ff;
  background-color: #bcbdf0;
  box-shadow: rgb(0 0 0 / 15%) 0px 3px 3px 2px;
  border-radius: 5px;
  padding: 10px;
  margin: 10px 0;
}

.darker {
  border-color: #a8a4a4;
  background-color: #7e73fa;
}

.container::after {
  content: "";
  clear: both;
  display: table;
}

.container img {
  float: left;
  max-width: 60px;
  width: 100%;
  margin-right: 20px;
  border-radius: 50%;
}

.container img.right {
  float: right;
  margin-left: 20px;
  margin-right:0;
}

.time-right {
  float: right;
  color: #fcf7f7;
}

.time-left {
  float: left;
  color: #251f1f;
}
#chat-container {
    /* Existing styles... */
    overflow-y: auto;
    height: 400px;  /* Adjust height as needed */
}
</style>
</head>
<body>
  <script>
    window.onload = function() {
        var chatContainer = document.getElementById("chat-container");  // Replace with your container element ID
        if (chatContainer) {
            chatContainer.scrollTop = chatContainer.scrollHeight;  // Scroll to bottom
        } 
        window.scrollTo(0, document.documentElement.scrollHeight);
    };
  </script>

<h2>Chat Room</h2>
<div id="chat-container">
  {% for message in messages %}
    {% if message.sender == request.user %}
      <div class="container darker">
        <img src="https://res.cloudinary.com/dqnwkkmzz/image/upload/v1/media/post-pic/default_dp.png" alt="Avatar" class="right" style="width:100%;">
        <p>{{message.sender}}</p>
        <p>{{message.content}}</p>
        <span class="time-left">11:01</span>
      </div>
    {% else %}
      <div class="container">
        <img src="https://res.cloudinary.com/dqnwkkmzz/image/upload/v1/media/post-pic/default_dp.png" alt="Avatar" style="width:100%;">
        <p>{{message.sender}}</p>
        <p>{{message.content}}</p>
        <span class="time-right">11:00</span>
      </div>
    {% endif %}
  {% endfor %}

</div> 
<div class="chat-input-container">
  <textarea id="message-input" placeholder="Type your message..." rows="1"></textarea>
  <button id="send-message-button">Send</button>
</div>
{{room_name|json_script:"room-name"}}
{{request.user.username|json_script:"user_username"}}

<script>
  const roomName = JSON.parse(document.getElementById('room-name').textContent);
  const user_username = JSON.parse(document.getElementById('user_username').textContent);

  document.querySelector("#send-message-button").onclick = function(e){
    const messageInputDOM = document.querySelector('#message-input');
    const message = messageInputDOM.value;
     chatSocket.send(JSON.stringify({
      'message': message,
      'username':user_username,
    }))
    messageInputDOM.value="";
  }
  console.log('ws://'+ window.location.host+'/ws/chat/'+roomName+'/')
  const chatSocket = new WebSocket (
      'ws://'+ window.location.host+'/ws/chat/'+roomName+'/'
  );

  
  chatSocket.onmessage = function(e){
      const data = JSON.parse(e.data);
      console.log(data);

      const messageElement = document.createElement('div');
      messageElement.classList.add('container');
      new_message_string= `<img src="https://res.cloudinary.com/dqnwkkmzz/image/upload/v1/media/post-pic/default_dp.png" alt="Avatar" style="width:100%;">
        <p>`+data.username+`</p>
        <p>`+data.message+`</p>
        <span class="time-right">11:00</span>`;
      if (data.username == user_username){
        messageElement.classList.add('darker');
        new_message_string= `<img src="https://res.cloudinary.com/dqnwkkmzz/image/upload/v1/media/post-pic/default_dp.png" alt="Avatar" class="right" style="width:100%;">
        <p>`+data.username+`</p>
        <p>`+data.message+`</p>
        <span class="time-right">11:00</span>`; 
        
      }

      
      messageElement.innerHTML= new_message_string;
      const chatContainer = document.querySelector('#chat-container');
      chatContainer.appendChild(messageElement);

      chatContainer.scrollTop = chatContainer.scrollHeight;
  };
</script>
</body>
</html>
