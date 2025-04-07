import React from 'react';

const Footer = () => {
  return (
    <footer className="w-full h-[300px] bg-beige-100 flex items-center justify-center">
      <div className="grid grid-cols-3 gap-8">
        <div>
          <h3 className="font-bold mb-2">Navigation</h3>
          <a href="#about" className="block hover:text-gray-600">About</a>
          <a href="#expertise" className="block hover:text-gray-600">Expertise</a>
          <a href="#gallery" className="block hover:text-gray-600">Gallery</a>
        </div>
        <div>
          <h3 className="font-bold mb-2">Contact</h3>
          <p>Email: info@spacex.com</p>
          <p>Phone: +1 123 456 7890</p>
        </div>
        <div>
          <h3 className="font-bold mb-2">Follow Us</h3>
          <a href="#" className="block hover:text-gray-600">Twitter</a>
          <a href="#" className="block hover:text-gray-600">Instagram</a>
        </div>
      </div>
      <div className="absolute bottom-8 text-4xl font-serif">SpaceX</div>
    </footer>
  );
};

export default Footer;