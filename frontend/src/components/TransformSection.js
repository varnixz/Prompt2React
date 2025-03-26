import React from 'react';
import styled from 'styled-components';

const Container = styled.section`
  padding: 100px 20px;
  background: #f8f9fa;
`;

const Content = styled.div`
  max-width: 1200px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 60px;
  align-items: center;
`;

const TextContent = styled.div`
  h2 {
    font-size: 2.5rem;
    margin-bottom: 20px;
    color: #333;
  }

  p {
    color: #666;
    line-height: 1.6;
  }
`;

const Features = styled.div`
  margin-top: 30px;
`;

const Feature = styled.div`
  margin-bottom: 20px;
  h3 {
    font-size: 1.2rem;
    color: #6c63ff;
    margin-bottom: 10px;
  }
`;

const ImageContainer = styled.div`
  img {
    width: 100%;
    border-radius: 10px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  }
`;

const TransformSection = () => {
  return (
    <Container>
      <Content>
        <TextContent>
          <h2>Website Prompt Converter</h2>
          <p>[Your platform description here]</p>
          <Features>
            <Feature>
              <h3>Real-Time Preview</h3>
              <p>[Feature description here]</p>
            </Feature>
            <Feature>
              <h3>User-Friendly Interface</h3>
              <p>[Feature description here]</p>
            </Feature>
            <Feature>
              <h3>Customizable Templates</h3>
              <p>[Feature description here]</p>
            </Feature>
          </Features>
        </TextContent>
        <ImageContainer>
          <img src="[Your feature image URL]" alt="Platform features" />
        </ImageContainer>
      </Content>
    </Container>
  );
};

export default TransformSection;