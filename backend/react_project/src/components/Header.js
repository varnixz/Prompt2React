import React from 'react';

const Header = () => {
  return (
    <header className="fixed top-0 left-0 w-full h-20 bg-transparent flex items-center justify-between px-8 z-50">
      <nav className="flex space-x-6 uppercase text-sm">
        <a href="#about" className="hover:text-gray-600">About</a>
        <a href="#expertise" className="hover:text-gray-600">Expertise</a>
        <a href="#gallery" className="hover:text-gray-600">Gallery</a>
      </nav>
      <div className="text-2xl font-serif">SpaceX</div>
      <div className="flex space-x-4">
        <a href="#" className="hover:text-gray-600">Twitter</a>
        <a href="#" className="hover:text-gray-600">Instagram</a>
      </div>
    </header>
  );
};

export default Header;