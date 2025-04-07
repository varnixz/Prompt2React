import React from 'react';

const About = () => {
  return (
    <section id="about" className="h-[600px] flex items-center justify-center bg-white">
      <div className="w-1/2">
        <img src="https://images.pexels.com/photos/7666421/pexels-photo-7666421.jpeg?auto=compress&cs=tinysrgb&w=x600&h=x600&fit=crop" alt="SpaceX mission" className="w-full h-auto" />
      </div>
      <div className="w-1/2 pl-8">
        <p className="text-xl font-serif italic">
          SpaceX is revolutionizing space technology, with the ultimate goal of enabling people to live on other planets.
        </p>
        <img src="https://images.pexels.com/photos/30918009/pexels-photo-30918009.jpeg?auto=compress&cs=tinysrgb&w=x50&h=x50&fit=crop" alt="Elon Musk signature" className="mt-4" />
      </div>
    </section>
  );
};

export default About;