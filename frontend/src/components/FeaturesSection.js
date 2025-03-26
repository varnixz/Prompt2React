import React from 'react';
import styled from 'styled-components';

const Section = styled.div`
  padding: 80px 20px;
  background: #f8f9fa;
`;

const Container = styled.div`
  max-width: 1200px;
  margin: 0 auto;
  text-align: center;
`;

const Title = styled.h2`
  font-size: 2.5rem;
  color: #333;
  margin-bottom: 20px;
`;

const Description = styled.p`
  color: #666;
  font-size: 1.1rem;
  max-width: 800px;
  margin: 0 auto 60px;
  line-height: 1.6;
`;

const ContentGrid = styled.div`
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 60px;
  align-items: center;
  margin-top: 40px;
`;

const ImageContainer = styled.div`
  img {
    width: 100%;
    border-radius: 10px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease;

    &:hover {
      transform: translateY(-5px);
    }
  }
`;

const FeaturesContainer = styled.div`
  text-align: left;
`;

const Feature = styled.div`
  margin-bottom: 30px;
  padding: 20px;
  background: white;
  border-radius: 10px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
  transition: transform 0.3s ease;

  &:hover {
    transform: translateY(-3px);
  }

  h3 {
    font-size: 1.3rem;
    color: #333;
    margin-bottom: 10px;
  }

  p {
    color: #666;
    line-height: 1.6;
  }
`;

const FeaturesSection = () => {
  return (
    <Section>
      <Container>
        <Title>Website Prompt Converter</Title>
        <Description>
          Transform your ideas into stunning websites effortlessly with our innovative prompt
          conversion service.
        </Description>
        
        <ContentGrid>
          <ImageContainer>
            <img 
              src="https://images.pexels.com/photos/5908814/pexels-photo-5908814.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2" 
              alt="Website Preview"
            />
          </ImageContainer>
          
          <FeaturesContainer>
            <Feature>
              <h3>Real-Time Preview</h3>
              <p>See your website changes instantly with our live preview feature
                for perfect adjustments.</p>
            </Feature>
            
            <Feature>
              <h3>User-Friendly Interface</h3>
              <p>Easily navigate and create websites with our intuitive design
                tools and features.</p>
            </Feature>
            
            <Feature>
              <h3>Customizable Templates</h3>
              <p>Choose from a variety of templates to suit your unique website
                needs and style.</p>
            </Feature>
          </FeaturesContainer>
        </ContentGrid>
      </Container>
    </Section>
  );
};

export default FeaturesSection;