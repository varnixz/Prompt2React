import React from 'react';
import { FaGithub, FaLinkedin } from 'react-icons/fa';

const Header = () => {
  return (
    <header className="fixed top-0 left-0 w-full h-20 flex items-center justify-between px-8 bg-transparent z-50">
      <nav className="flex space-x-6 uppercase text-sm">
        <a href="#about" className="hover:text-gray-600">About</a>
        <a href="#expertise" className="hover:text-gray-600">Expertise</a>
        <a href="#gallery" className="hover:text-gray-600">Gallery</a>
      </nav>
      <div className="text-2xl font-serif">LudoGame</div>
      <div className="flex space-x-4">
        <a href="https://github.com" aria-label="Github"><FaGithub className="text-xl hover:text-gray-600" /></a>
        <a href="https://linkedin.com" aria-label="LinkedIn"><FaLinkedin className="text-xl hover:text-gray-600" /></a>
      </div>
    </header>
  );
};

export default Header;