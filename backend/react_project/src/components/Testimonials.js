import React from 'react';

const Testimonials = () => {
  return (
    <section className="h-[400px] bg-white p-8">
      <h2 className="text-3xl font-bold text-center mb-8">Testimonials</h2>
      <div className="flex justify-center space-x-8">
        {[1, 2, 3].map((index) => (
          <div key={index} className="w-[400px] h-[150px] bg-gray-200 p-6 rounded-lg">
            <p className="italic">"Lorem ipsum dolor sit amet, consectetur adipiscing elit."</p>
            <p className="font-bold mt-2">- Client {index}</p>
          </div>
        ))}
      </div>
    </section>
  );
};

export default Testimonials;