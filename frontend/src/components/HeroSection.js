import React from 'react';
import styled from 'styled-components';
import { Link } from 'react-scroll';

const HeroContainer = styled.div`
  height: 100vh;
  position: relative;
  overflow: hidden;
  width: 100%;
`;

const VideoBackground = styled.video`
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: 0;
`;

const Overlay = styled.div`
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    to bottom,
    rgba(0, 0, 0, 0.7),
    rgba(0, 0, 0, 0.8)
  );
  z-index: 1;
`;

const Content = styled.div`
  position: relative;
  z-index: 2;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  color: white;
  padding: 0 20px;
`;

const Title = styled.h1`
  font-size: 4rem;
  margin-bottom: 20px;
  color: white;
  font-weight: bold;
`;

const Subtitle = styled.p`
  font-size: 1.5rem;
  margin-bottom: 40px;
  max-width: 800px;
  color: rgba(255, 255, 255, 0.9);
`;

const StartButton = styled(Link)`
  padding: 15px 40px;
  background: #8B728E;
  color: white;
  border: none;
  border-radius: 30px;
  font-size: 1.2rem;
  cursor: pointer;
  transition: all 0.3s ease;
  text-decoration: none;
  display: inline-block;

  &:hover {
    transform: translateY(-3px);
    background: #7a6179;
    box-shadow: 0 5px 15px rgba(139, 114, 142, 0.3);
  }
`;

const HeroSection = () => {
  return (
    <HeroContainer>
      <VideoBackground autoPlay loop muted playsInline>
        <source src="https://videos.pexels.com/video-files/6248605/6248605-uhd_2560_1440_25fps.mp4" type="video/mp4" />
      </VideoBackground>
      <Overlay />
      <Content>
        <Title>Transform Your Ideas into Stunning Websites</Title>
        <Subtitle>
          Easily convert prompts into beautiful, functional websites with our
          intuitive platform and tools.
        </Subtitle>
        <StartButton to="prompt-section" smooth={true} duration={800}>
          Get Started
        </StartButton>
      </Content>
    </HeroContainer>
  );
};

export default HeroSection;