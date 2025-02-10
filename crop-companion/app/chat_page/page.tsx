'use client';
import { useState, useEffect, useRef } from "react";
import { Send } from "lucide-react";
import Sidebar from "@/components/Sidebar";

export default function Page() {
  const [messages, setMessages] = useState([
    { role: "assistant", content: "Hello! How can I assist you today?" },
  ]);
  const [input, setInput] = useState("");
  const chatEndRef = useRef(null);

  const [loading, setLoading] = useState(false);

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);


  // Logic to connect chat and server
  const sendMessage = async () => {
    if (!input.trim()) return;
  
    setMessages((prev) => [...prev, { role: "user", content: input }]);
    setInput("");
    setLoading(true);
  
    try {
      const token = "token"; // Replace with your actual token
      const response = await fetch("http://localhost:8000/generate", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqb2huZG9lIiwiZXhwIjoxNzM5MTUxMDg3fQ.vBHLbMj2kBBeWBhwQNpsLxg1o6mxSMBxuAzcNx0sEkc`, // Add Authorization header
        },
        body: JSON.stringify({
          prompt: input,
          system: "You help farmers achieve their goals of sustainable farming.",
          model: "llama3.2:1b",
          stream: true, // Enable streaming
          username: "johndoe", // Add username
        }),
      });
  
      if (!response.ok) throw new Error("Failed to generate response");
  
      const reader = response.body?.getReader();
      const decoder = new TextDecoder();
      let assistantResponse = "";
  
      if (reader) {
        while (true) {
          const { done, value } = await reader.read();
          if (done) break;
          const chunk = decoder.decode(value, { stream: true });
          assistantResponse += chunk;
  
          // Update messages in real time
          setMessages((prev) => {
            const lastMessage = prev[prev.length - 1];
            if (lastMessage?.role === "assistant") {
              return [
                ...prev.slice(0, -1),
                { role: "assistant", content: lastMessage.content + chunk },
              ];
            } else {
              return [...prev, { role: "assistant", content: chunk }];
            }
          });
        }
      }
    } catch (error) {
      console.error("Error:", error);
    } finally {
      setLoading(false);
    }
  };

  const handleNewChat = () => {
    setMessages([
      { role: "assistant", content: "Hello! How can I assist you today?" },
    ]);
    setInput("");
  };
  
  
  return (
    <div className="flex h-screen">
      <Sidebar onNewChat={handleNewChat} />
      <div className="flex flex-col flex-1 bg-gray-900 text-white">
        <div className="flex-1 overflow-y-auto p-4 space-y-4 flex flex-col">
          {messages.map((msg, index) => (
            <div
              key={index}
              className={`p-3 rounded-lg max-w-xs ${
                msg.role === "user"
                  ? "bg-blue-600 text-white self-end"
                  : "bg-gray-700 text-white self-start"
              }`}
            >
              {msg.content}
            </div>
          ))}
          <div ref={chatEndRef} />
        </div>
        <div className="p-4 bg-gray-800 border-t border-gray-700 flex items-center">
          <input
            type="text"
            className="flex-1 p-2 bg-gray-700 border border-gray-600 rounded-lg focus:outline-none text-white"
            placeholder="Type a message..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && sendMessage()}
          />
          <button
            className="ml-2 p-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
            onClick={sendMessage}
          >
            <Send size={20} />
          </button>
        </div>
      </div>
    </div>
  );
}