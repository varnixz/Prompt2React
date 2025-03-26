import React from 'react';
import Header from './components/Header';
import Hero from './components/Hero';
import Services from './components/Services';
import Features from './components/Features';
import Highlights from './components/Highlights';
import Testimonials from './components/Testimonials';
import Footer from './components/Footer';

const App = () => {
  return (
    <div>
      <Header />
      <Hero />
      <Services />
      <Features />
      <Highlights />
      <Testimonials />
      <Footer />
    </div>
  );
};

export default App;