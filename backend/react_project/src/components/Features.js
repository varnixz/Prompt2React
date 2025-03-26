import React from 'react';

const Features = () => {
  return (
    <section className="h-[500px] bg-light-gray flex items-center justify-between px-8">
      <div className="w-1/2">
        <h2 className="text-3xl font-bold mb-4">Why Choose Us?</h2>
        <p className="text-lg">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
      </div>
      <div className="w-1/2">
        <img src="https://images.pexels.com/photos/31260029/pexels-photo-31260029.jpeg?auto=compress&cs=tinysrgb&w=500&h=500&fit=crop" alt="features" className="w-full h-auto rounded-lg" />
      </div>
    </section>
  );
};

export default Features;