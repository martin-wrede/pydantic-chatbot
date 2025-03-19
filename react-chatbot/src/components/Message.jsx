// filepath: c:\Users\marti\OneDrive\Documents\CODING\pydantic-ai-tutorial-rabbitmetrics\react-chatbot\src\components\Message.jsx
import React from 'react';

const Message = ({ text, sender }) => {
  return (
    <div className={`message ${sender}`}>
      <p>{text}</p>
    </div>
  );
};

export default Message;