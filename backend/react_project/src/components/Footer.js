import React from 'react';

const Footer = () => {
  return (
    <footer className="h-[300px] bg-black text-white flex flex-col items-center justify-center px-8">
      <div className="text-2xl font-bold text-gold mb-4">University</div>
      <div className="flex space-x-8 mb-4">
        <a href="#" className="hover:text-gold">Phone: 123-456-7890</a>
        <a href="#" className="hover:text-gold">Email: info@university.com</a>
      </div>
      <div className="flex space-x-8 mb-4">
        <a href="#" className="hover:text-gold">Home</a>
        <a href="#" className="hover:text-gold">About</a>
        <a href="#" className="hover:text-gold">Services</a>
        <a href="#" className="hover:text-gold">Contact</a>
      </div>
      <p className="text-sm">© 2023 University. All rights reserved.</p>
    </footer>
  );
};

export default Footer;