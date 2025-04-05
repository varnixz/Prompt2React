import React from 'react';

const About = () => {
  return (
    <section id="about" className="h-[600px] flex items-center px-8 bg-white">
      <div className="w-1/2">
        <img src="https://images.pexels.com/photos/2681319/pexels-photo-2681319.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop" alt="about" className="w-full h-auto rounded-lg shadow-lg" />
      </div>
      <div className="w-1/2 pl-8">
        <p className="text-xl font-serif italic">
          LudoGame is a modern take on the classic board game, designed for players of all ages. <br />
          <span className="font-bold">Play anytime, anywhere!</span>
        </p>
        <img src="https://images.pexels.com/photos/48148/pexels-photo-48148.jpeg?auto=compress&cs=tinysrgb&w=200&h=100&fit=crop" alt="signature" className="mt-8 w-40 h-auto" />
      </div>
    </section>
  );
};

export default About;