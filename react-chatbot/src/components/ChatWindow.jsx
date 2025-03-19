// filepath: c:\Users\marti\OneDrive\Documents\CODING\pydantic-ai-tutorial-rabbitmetrics\react-chatbot\src\components\ChatWindow.jsx
import React, { useState } from 'react';
import Message from './Message';
import Input from './Input';

const ChatWindow = () => {
  const [messages, setMessages] = useState([]);

  const handleSendMessage = async (message) => {
    setMessages([...messages, { text: message, sender: 'user' }]);
    
    // Call the backend API
    const response = await fetch('http://localhost:8000/chat', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ user_input: message }),
    });

    const data = await response.json();
    setMessages([...messages, { text: message, sender: 'user' }, { text: data.response, sender: 'bot' }]);
  };

  return (
    <div className="chat-window">
      <div className="messages">
        {messages.map((msg, index) => (
          <Message key={index} text={msg.text} sender={msg.sender} />
        ))}
      </div>
      <Input onSendMessage={handleSendMessage} />
    </div>
  );
};

export default ChatWindow;