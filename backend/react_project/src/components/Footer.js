import React from 'react';
import { FaGithub, FaLinkedin } from 'react-icons/fa';

const Footer = () => {
  return (
    <footer className="w-full h-[300px] bg-beige-100 flex flex-col justify-center">
      <div className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-6xl mx-auto px-8">
        <div>
          <h3 className="font-serif text-xl mb-4">Navigation</h3>
          <ul>
            <li><a href="#about" className="hover:text-gray-600">About</a></li>
            <li><a href="#expertise" className="hover:text-gray-600">Expertise</a></li>
            <li><a href="#gallery" className="hover:text-gray-600">Gallery</a></li>
          </ul>
        </div>
        <div>
          <h3 className="font-serif text-xl mb-4">Contact</h3>
          <p>Email: info@ludogame.com</p>
          <p>Phone: +123 456 7890</p>
          <p>Location: 123 Game Street, Fun City</p>
        </div>
        <div>
          <h3 className="font-serif text-xl mb-4">Follow Us</h3>
          <div className="flex space-x-4">
            <a href="https://github.com" aria-label="Github"><FaGithub className="text-xl hover:text-gray-600" /></a>
            <a href="https://linkedin.com" aria-label="LinkedIn"><FaLinkedin className="text-xl hover:text-gray-600" /></a>
          </div>
        </div>
      </div>
      <div className="text-center mt-8">
        <p className="font-serif text-4xl">LudoGame</p>
      </div>
    </footer>
  );
};

export default Footer;