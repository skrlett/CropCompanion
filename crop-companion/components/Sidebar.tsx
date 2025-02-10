import React from 'react';
import { MessageSquare, Plus, Settings, Trash } from 'lucide-react';

const Sidebar = ({ onNewChat }) => {
  // Dummy chat history data
  const chatHistory = [
    {
      id: 1,
      title: "Organic Farming Methods",
      preview: "Discussion about sustainable pest control...",
      date: "2024-02-09"
    },
    {
      id: 2,
      title: "Crop Rotation Planning",
      preview: "Seasonal rotation schedule for vegetables...",
      date: "2024-02-08"
    },
    {
      id: 3,
      title: "Soil Health Analysis",
      preview: "Tips for maintaining soil nutrients...",
      date: "2024-02-07"
    }
  ];

  return (
    <div className="w-64 h-screen bg-gray-800 text-white flex flex-col">
      {/* New Chat Button */}
      <button 
        onClick={onNewChat}
        className="flex items-center gap-2 p-3 m-2 rounded-lg bg-blue-600 hover:bg-blue-700 transition-colors"
      >
        <Plus size={16} />
        New Chat
      </button>

      {/* Chat History */}
      <div className="flex-1 overflow-y-auto">
        {chatHistory.map((chat) => (
          <div
            key={chat.id}
            className="p-3 m-2 rounded-lg hover:bg-gray-700 cursor-pointer transition-colors"
          >
            <div className="flex items-center gap-2">
              <MessageSquare size={16} />
              <div className="flex-1">
                <h3 className="text-sm font-medium truncate">{chat.title}</h3>
                <p className="text-xs text-gray-400 truncate">{chat.preview}</p>
              </div>
            </div>
          </div>
        ))}
      </div>

      {/* Bottom Section */}
      <div className="border-t border-gray-700 p-2">
        <button className="flex items-center gap-2 p-2 w-full rounded-lg hover:bg-gray-700 transition-colors">
          <Trash size={16} />
          Clear History
        </button>
        <button className="flex items-center gap-2 p-2 w-full rounded-lg hover:bg-gray-700 transition-colors">
          <Settings size={16} />
          Settings
        </button>
      </div>
    </div>
  );
};

export default Sidebar;