import React from 'react';

const Contact = () => (
  <section id="contact" className="py-20 bg-white">
    <div className="max-w-4xl mx-auto text-center">
      <h2 className="text-3xl italic mb-8">Contact Us</h2>
      <form className="space-y-4">
        <input type="text" placeholder="Name" className="w-full p-2 border rounded" />
        <input type="email" placeholder="Email" className="w-full p-2 border rounded" />
        <button type="submit" className="bg-black text-white px-6 py-2 rounded hover:bg-gray-800 transition duration-300">Subscribe Now</button>
      </form>
    </div>
  </section>
);

export default Contact;