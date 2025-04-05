import React from 'react';
import { useState } from 'react';

const Hero = () => {
  const [currentImage, setCurrentImage] = useState(0);
  const images = [
    'https://via.placeholder.com/800x600',
    'https://via.placeholder.com/800x600',
    'https://via.placeholder.com/800x600',
  ];

  const nextImage = () => {
    setCurrentImage((prev) => (prev === images.length - 1 ? 0 : prev + 1));
  };

  const prevImage = () => {
    setCurrentImage((prev) => (prev === 0 ? images.length - 1 : prev - 1));
  };

  return (
    <section className="h-screen flex flex-col items-center justify-center bg-gray-100">
      <h1 className="text-5xl font-serif text-black mb-4">Welcome to LudoGame</h1>
      <p className="text-lg mb-8">The ultimate board game experience</p>
      <div className="relative w-full max-w-3xl">
        <img src={images[currentImage]} alt="game" className="w-full h-auto rounded-lg shadow-lg" />
        <button onClick={prevImage} className="absolute left-4 top-1/2 transform -translate-y-1/2 bg-white p-2 rounded-full shadow-lg">&#10094;</button>
        <button onClick={nextImage} className="absolute right-4 top-1/2 transform -translate-y-1/2 bg-white p-2 rounded-full shadow-lg">&#10095;</button>
      </div>
    </section>
  );
};

export default Hero;