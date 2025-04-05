import React from 'react';

const Expertise = () => {
  const expertiseItems = ['Strategy', 'Fun', 'Competition', 'Social'];

  return (
    <section id="expertise" className="w-full py-16 bg-beige-100">
      <div className="max-w-4xl mx-auto text-center">
        {expertiseItems.map((item, index) => (
          <h2 key={index} className="text-4xl font-bold uppercase mb-8 hover:text-gray-600 transition-all cursor-pointer">
            {item}
          </h2>
        ))}
      </div>
    </section>
  );
};

export default Expertise;