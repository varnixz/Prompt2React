import React from 'react';

const Hero = () => {
  return (
    <section className="h-screen flex items-center justify-between px-8 bg-dark">
      <div className="w-1/2">
        <h1 className="text-4xl font-bold uppercase text-white mb-4">Welcome to Our University</h1>
        <button className="bg-gold text-white px-8 py-3 rounded-full hover:bg-dark-gold">Apply Now</button>
      </div>
      <div className="w-1/2 relative">
        <img src="https://images.pexels.com/photos/159490/pexels-photo-159490.jpeg?auto=compress&cs=tinysrgb&w=600&h=300&fit=crop" alt="campus" className="w-full h-auto rounded-lg" />
      </div>
    </section>
  );
};

export default Hero;