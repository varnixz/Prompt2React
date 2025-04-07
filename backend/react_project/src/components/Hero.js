import React from 'react';

const Hero = () => {
  const images = Array(3).fill({ src: 'https://images.pexels.com/photos/60130/pexels-photo-60130.jpeg?auto=compress&cs=tinysrgb&w=x600&h=x600&fit=crop', alt: 'SpaceX rocket' });

  return (
    <section className="h-screen flex flex-col items-center justify-center bg-gray-100">
      <h1 className="text-5xl font-serif mb-4">Exploring the Cosmos</h1>
      <p className="text-lg mb-8">Discover the future of space travel.</p>
      <div className="w-3/4 overflow-hidden relative">
        <div className="flex transition-transform duration-500">
          {images.map((img, index) => (
            <img key={index} src={img.src} alt={img.alt} className="w-full h-auto" />
          ))}
        </div>
        <button className="absolute top-1/2 left-0 transform -translate-y-1/2 bg-black text-white p-2">←</button>
        <button className="absolute top-1/2 right-0 transform -translate-y-1/2 bg-black text-white p-2">→</button>
      </div>
    </section>
  );
};

export default Hero;