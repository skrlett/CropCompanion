import React, { useEffect } from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import Contact from './Contact';
import './App.css';

function App() {
  useEffect(() => {
    const handleMouseMove = (e) => {
      const cards = document.querySelectorAll('.card');
      cards.forEach((card) => {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        card.style.setProperty('--mouse-x', `${x}px`);
        card.style.setProperty('--mouse-y', `${y}px`);
      });
    };

    document.addEventListener('mousemove', handleMouseMove);
    return () => document.removeEventListener('mousemove', handleMouseMove);
  }, []);

  return (
    <Router>
      <div className="app">
        {/* Header */}
        <header className="header">
          <div className="logo">AgriAI</div>
          <nav>
            <ul>
              <li><Link to="/">Home</Link></li>
              <li><Link to="/contact">Contact</Link></li>
            </ul>
          </nav>
        </header>

        <Routes>
          <Route
            path="/"
            element={
              <>
                {/* Hero Section */}
                <section className="hero" id="home">
                  <div className="hero-content">
                    <h1>Optimize Your Crop Yield with AI</h1>
                    <p>Our AI-driven solutions provide real-time insights and recommendations to maximize your farming potential.</p>
                    <Link to="/contact" className="cta-button">Get Started</Link>
                  </div>
                </section>

                {/* About Section */}
                <section className="about" id="about">
                  <h2>About the Product</h2>
                  <p>The Crop Yield Optimization Model leverages AI to analyze soil, weather, and crop data, providing actionable insights for farmers.</p>
                </section>

                {/* How It Works Section */}
                <section className="how-it-works" id="how">
                  <h2>How It Works</h2>
                  <div className="card-container">
                    <div className="card">
                      <h3>Data Collection</h3>
                      <p>Gather soil, weather, and crop data for analysis.</p>
                    </div>
                    <div className="card">
                      <h3>Machine Learning Optimization</h3>
                      <p>AI models analyze data to optimize crop yield predictions.</p>
                    </div>
                    <div className="card">
                      <h3>Real-time Chatbot Guidance</h3>
                      <p>Receive personalized farming advice from our AI-powered chatbot.</p>
                    </div>
                  </div>
                </section>

                {/* Features Section */}
                <section className="features" id="features">
                  <h2>Key Features</h2>
                  <div className="card-container">
                    <div className="card">
                      <h3>Accurate Predictions</h3>
                      <p>Our AI forecasts crop yields with high accuracy based on real-time data.</p>
                    </div>
                    <div className="card">
                      <h3>Real-time Assistance</h3>
                      <p>Instant responses and tailored advice from our AI chatbot.</p>
                    </div>
                    <div className="card">
                      <h3>Sustainability Focused</h3>
                      <p>Enhance farming practices while reducing environmental impact.</p>
                    </div>
                  </div>
                </section>
              </>
            }
          />
          <Route path="/contact" element={<Contact />} />
        </Routes>

        {/* Footer */}
        <footer className="footer">
          <p>&copy; 2025 AgriAI. All rights reserved.</p>
        </footer>
      </div>
    </Router>
  );
}

export default App;