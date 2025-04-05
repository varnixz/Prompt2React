import React from 'react';

const Gallery = () => {
  const images = [
    'https://via.placeholder.com/300x200',
    'https://via.placeholder.com/300x200',
    'https://via.placeholder.com/300x200',
    'https://via.placeholder.com/300x200',
    'https://via.placeholder.com/300x200',
    'https://via.placeholder.com/300x200',
  ];

  return (
    <section id="gallery" className="w-full py-16 bg-white">
      <div className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-6xl mx-auto px-8">
        {images.map((image, index) => (
          <div key={index} className="relative overflow-hidden rounded-lg shadow-lg hover:scale-105 transition-transform">
            <img src={image} alt="gallery" className="w-full h-auto" />
            <p className="absolute bottom-0 left-0 w-full p-4 bg-black bg-opacity-50 text-white font-serif text-center">Game {index + 1}</p>
          </div>
        ))}
      </div>
    </section>
  );
};

export default Gallery;