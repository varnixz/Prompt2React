import React from 'react';

const Header = () => {
  return (
    <header className="h-20 w-full bg-white flex items-center justify-between px-8">
      <div className="text-2xl font-bold text-gold">University</div>
      <nav className="flex space-x-8 uppercase">
        <a href="#" className="text-black hover:text-gold">Home</a>
        <a href="#" className="text-black hover:text-gold">About</a>
        <a href="#" className="text-black hover:text-gold">Services</a>
        <a href="#" className="text-black hover:text-gold">Contact</a>
      </nav>
      <button className="bg-gold text-white px-6 py-2 rounded-full hover:bg-dark-gold">Contact Us</button>
    </header>
  );
};

export default Header;