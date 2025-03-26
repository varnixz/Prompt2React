import React from 'react';

const Highlights = () => {
  return (
    <section className="h-[600px] bg-white p-8">
      <h2 className="text-3xl font-bold text-center mb-8">Highlights</h2>
      <div className="grid grid-cols-2 gap-8">
        {[1, 2, 3, 4].map((index) => (
          <div key={index} className="relative">
            <img src="https://images.pexels.com/photos/2574619/pexels-photo-2574619.jpeg?auto=compress&cs=tinysrgb&w=300&h=250&fit=crop" alt="highlight" className="w-full h-auto rounded-lg" />
            <div className="absolute bottom-0 left-0 bg-gold p-4 w-full">
              <h3 className="text-lg font-bold">Highlight {index}</h3>
              <p className="text-sm">Lorem ipsum dolor sit amet.</p>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
};

export default Highlights;