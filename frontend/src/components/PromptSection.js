import React, { useState } from 'react';
import styled from 'styled-components';

const Section = styled.section`
  min-height: 100vh;
  padding: 100px 20px;
  background: #F0EEF2;
  display: flex;
  align-items: center;
  justify-content: center;
`;

const Container = styled.div`
  max-width: 800px;
  width: 100%;
  padding: 40px;
  background: white;
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(139, 114, 142, 0.1);
`;

const TextArea = styled.textarea`
  width: 100%;
  height: 200px;
  padding: 20px;
  border: 2px solid #e0e0e0;
  border-radius: 10px;
  font-size: 16px;
  resize: vertical;
  transition: all 0.3s ease;

  &:focus {
    outline: none;
    border-color: #8B728E;
  }
`;

const Title = styled.h2`
  font-size: 2.5rem;
  color: #333;
  margin-bottom: 30px;
  text-align: center;
`;

const Form = styled.form`
  display: flex;
  flex-direction: column;
  gap: 20px;
`;

// ... previous styled components ...

const Button = styled.button`
  padding: 15px 40px;
  background: #8B728E;
  color: white;
  border: none;
  border-radius: 30px;
  font-size: 1.1rem;
  cursor: pointer;
  transition: all 0.3s ease;
  align-self: center;

  &:hover {
    background: #7a6179;
    transform: translateY(-2px);
  }

  &:disabled {
    background: #ccc;
    cursor: not-allowed;
    transform: none;
  }
`;

// ... rest of the component remains the same ...

const Message = styled.div`
  padding: 15px;
  border-radius: 8px;
  text-align: center;
  margin-top: 20px;

  &.error {
    background: #ffe6e6;
    color: #ff3333;
  }

  &.success {
    background: #e6ffe6;
    color: #00cc00;
  }
`;

const PromptSection = ({ onGenerate, isLoading, error, successMessage }) => {
  const [prompt, setPrompt] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    onGenerate(prompt);
  };

  return (
    <Section id="prompt-section">
      <Container>
        <Title>Generate Your Website</Title>
        <Form onSubmit={handleSubmit}>
          <TextArea
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            placeholder="Describe your dream website..."
            required
          />
          <Button type="submit" disabled={isLoading}>
            {isLoading ? 'Generating...' : 'Generate & Download'}
          </Button>
        </Form>
        {error && <Message className="error">{error}</Message>}
        {successMessage && <Message className="success">{successMessage}</Message>}
      </Container>
    </Section>
  );
};

export default PromptSection;