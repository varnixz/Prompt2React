import React from 'react';

const Gallery = () => {
  const images = Array(6).fill({ src: 'https://images.pexels.com/photos/383568/pexels-photo-383568.jpeg?auto=compress&cs=tinysrgb&w=x300&h=x300&fit=crop', alt: 'SpaceX gallery image' });

  return (
    <section id="gallery" className="w-full py-16 bg-white">
      <div className="grid grid-cols-3 gap-4 px-8">
        {images.map((img, index) => (
          <div key={index} className="overflow-hidden shadow-lg hover:scale-105 transition duration-300">
            <img src={img.src} alt={img.alt} className="w-full h-auto" />
            <p className="text-center mt-2 font-serif">Image {index + 1}</p>
          </div>
        ))}
      </div>
    </section>
  );
};

export default Gallery;