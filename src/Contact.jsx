import React from 'react';
import './App.css';

function Contact() {
  return (
    <div className="contact-page">
      <h2>Contact Us</h2>
      <p>Interested in optimizing your farming? Contact us for a demo!</p>
      <form className="contact-form">
        <input type="text" placeholder="Your Name" required />
        <input type="email" placeholder="Your Email" required />
        <textarea placeholder="Your Message" rows="5" required></textarea>
        <button type="submit" className="cta-button">Send Message</button>
      </form>
    </div>
  );
}

export default Contact;