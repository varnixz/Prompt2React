import React from 'react';

const Header = () => (
  <header className="fixed top-0 left-0 w-full h-20 bg-white shadow-md flex items-center justify-between px-8 z-50">
    <div className="text-xl font-bold font-poppins">STARTUP</div>
    <nav className="hidden md:flex space-x-8 uppercase text-sm font-montserrat">
      <a href="#about">About</a>
      <a href="#portfolio">Portfolio</a>
      <a href="#clients">Clients</a>
      <a href="#contact">Contact</a>
    </nav>
    <button className="md:hidden">☰</button>
  </header>
);

export default Header;