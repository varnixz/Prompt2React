import React from 'react';

const Expertise = () => {
  const expertiseItems = ['Rockets', 'Satellites', 'Space Travel'];

  return (
    <section id="expertise" className="w-full py-16 bg-beige-100">
      <div className="text-center space-y-8">
        {expertiseItems.map((item, index) => (
          <h2 key={index} className="text-4xl font-bold uppercase hover:text-gray-600 transition duration-300">
            {item}
          </h2>
        ))}
      </div>
    </section>
  );
};

export default Expertise;