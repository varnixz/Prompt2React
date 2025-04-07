import React from 'react';
import Header from './components/Header';
import Hero from './components/Hero';
import About from './components/About';
import Expertise from './components/Expertise';
import Gallery from './components/Gallery';
import Features from './components/Features';
import Footer from './components/Footer';

const App = () => {
  return (
    <div>
      <Header />
      <Hero />
      <About />
      <Expertise />
      <Gallery />
      <Features />
      <Footer />
    </div>
  );
};

export default App;