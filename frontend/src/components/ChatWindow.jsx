import React, { useState } from 'react';
import MessageList from './MessageList';
import MessageInput from './MessageInput';

const ChatWindow = () => {
  const [messages, setMessages] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  const handleSendMessage = async (text) => {
    const newMessage = { sender: 'user', text };
    setMessages(prevMessages => [...prevMessages, newMessage]);
    setIsLoading(true);

    try {
      const response = await fetch('http://localhost:5001/api/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: text }),
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const data = await response.json();
      const botResponse = { sender: 'bot', text: data.summary };
      setMessages(prevMessages => [...prevMessages, botResponse]);
    } catch (error) {
      console.error('Error fetching data:', error);
      const errorResponse = { sender: 'bot', text: 'Sorry, something went wrong.' };
      setMessages(prevMessages => [...prevMessages, errorResponse]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="chat-window">
      <h2>AI Agent Chat</h2>
      <MessageList messages={messages} isLoading={isLoading} />
      <MessageInput onSendMessage={handleSendMessage} />
    </div>
  );
};

export default ChatWindow;
