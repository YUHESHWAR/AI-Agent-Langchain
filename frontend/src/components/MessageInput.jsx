import React, { useState } from 'react';

const MessageInput = ({ onSendMessage }) => {
  const [text, setText] = useState('');

  const handleSend = () => {
    if (text.trim()) {
      onSendMessage(text);
      setText('');
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      handleSend();
    }
  };

  return (
    <div className="message-input">
      <input
        type="text"
        value={text}
        onChange={(e) => setText(e.target.value)}
        onKeyPress={handleKeyPress}
        placeholder="Type your message..."
      />
      <button onClick={handleSend}>Send</button>
    </div>
  );
};

export default MessageInput;
