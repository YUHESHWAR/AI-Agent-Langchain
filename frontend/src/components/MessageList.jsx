import React from 'react';
import Message from './Message';

const MessageList = ({ messages, isLoading }) => {
  return (
    <div className="message-list">
      {messages.map((message, index) => (
        <Message key={index} sender={message.sender} text={message.text} />
      ))}
      {isLoading && (
        <div className="message bot">
          <p><i>Typing...</i></p>
        </div>
      )}
    </div>
  );
};

export default MessageList;
