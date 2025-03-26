import React from 'react';
import styled from 'styled-components';

const Container = styled.section`
  padding: 100px 20px;
  background: #8B728E;
  color: white;
  text-align: center;
`;

const TestimonialCard = styled.div`
  max-width: 800px;
  margin: 0 auto;
  padding: 40px;
`;

const Stars = styled.div`
  color: #ffd700;
  font-size: 24px;
  margin-bottom: 20px;
`;

const Quote = styled.p`
  font-size: 1.5rem;
  line-height: 1.6;
  margin-bottom: 30px;
`;

const Author = styled.div`
  img {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    margin-bottom: 10px;
  }
  
  h4 {
    font-size: 1.2rem;
    margin: 0;
  }
`;

const TestimonialSection = () => {
  return (
    <Container>
      <TestimonialCard>
        <Stars>★★★★★</Stars>
        <Quote>Varnix transformed my ideas into a stunning website effortlessly. The user-friendly interface made it easy to navigate and create exactly what I envisioned. Highly recommend!</Quote>
        <Author>
          <img src="https://images.pexels.com/photos/5102905/pexels-photo-5102905.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2" alt="User profile" />
          <h4>Varnix</h4>
        </Author>
      </TestimonialCard>
    </Container>
  );
};

export default TestimonialSection;