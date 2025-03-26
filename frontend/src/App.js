import React, { useState } from 'react';
import styled, { createGlobalStyle } from 'styled-components';
import Sidebar from './components/Sidebar';
import { Element } from 'react-scroll';
import HeroSection from './components/HeroSection';
import PromptSection from './components/PromptSection';
import FeaturesSection from './components/FeaturesSection';
import TestimonialSection from './components/TestimonialSection';
import FooterSection from './components/FooterSection';

const GlobalStyle = createGlobalStyle`
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Lato', sans-serif;
  }
`;

const AppContainer = styled.div`
  min-height: 100vh;
  width: 100%;
`;

const MainContent = styled.div`
  width: 100%;
  background: white;
  position: relative;
`;

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL; // Fetch backend URL from .env

function App() {
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [successMessage, setSuccessMessage] = useState('');

  const handleGenerateCode = async (prompt) => {
    if (!prompt.trim()) {
      setError('Please enter a prompt');
      return;
    }

    setIsLoading(true);
    setError(null);
    setSuccessMessage('');

    try {
      const response = await fetch(`${BACKEND_URL}/generate-react/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Failed to generate React code');
      }

      const blob = await response.blob();
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'react_project.zip';
      document.body.appendChild(a);
      a.click();
      window.URL.revokeObjectURL(url);
      setSuccessMessage('React project generated and downloaded successfully!');
    } catch (err) {
      setError(err.message || 'Something went wrong! Please try again.');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <>
      <GlobalStyle />
      <AppContainer>
        <Sidebar isOpen={isSidebarOpen} setIsOpen={setIsSidebarOpen} />
        <MainContent>
          <Element name="home">
            <HeroSection />
          </Element>
          <Element name="prompt-section">
            <PromptSection 
              onGenerate={handleGenerateCode}
              isLoading={isLoading}
              error={error}
              successMessage={successMessage}
            />
          </Element>
          <Element name="features">
            <FeaturesSection />
          </Element>
          <Element name="testimonial">
            <TestimonialSection />
          </Element>
          <Element name="footer">
            <FooterSection />
          </Element>
        </MainContent>
      </AppContainer>
    </>
  );
}

export default App;
