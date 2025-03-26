import React from 'react';
import styled from 'styled-components';
import { FaFacebook, FaInstagram, FaTiktok, FaTwitter } from 'react-icons/fa';

const FooterContainer = styled.footer`
  background: #1e213a;
  color: white;
  padding: 60px 40px 30px;
`;

const FooterContent = styled.div`
  max-width: 1200px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 40px;
`;

const Column = styled.div`
  h3 {
    font-size: 1.5rem;
    margin-bottom: 20px;
    color: white;
  }

  p {
    color: rgba(255, 255, 255, 0.8);
    margin-bottom: 10px;
    font-size: 0.9rem;
  }
`;

const SocialLinks = styled.div`
  display: flex;
  gap: 20px;
  margin-top: 15px;

  a {
    color: white;
    font-size: 20px;
    transition: opacity 0.3s;

    &:hover {
      opacity: 0.8;
    }
  }
`;

const Input = styled.input`
  width: 100%;
  padding: 12px;
  border: none;
  border-radius: 5px;
  margin-bottom: 10px;
  background: white;
  color: #333;

  &::placeholder {
    color: #666;
  }
`;

const Button = styled.button`
  background: #9c89b8;
  color: white;
  border: none;
  padding: 12px 24px;
  border-radius: 5px;
  cursor: pointer;
  transition: background 0.3s;
  width: 100%;

  &:hover {
    background: #8a75a5;
  }
`;

const Copyright = styled.div`
  text-align: left;
  margin-top: 40px;
  padding-top: 20px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  color: rgba(255, 255, 255, 0.6);
  font-size: 0.9rem;
`;

const FooterSection = () => {
  return (
    <FooterContainer>
      <FooterContent>
        <Column>
          <h3>Explore</h3>
          <p>Transform your ideas into stunning websites effortlessly.</p>
          <SocialLinks>
            <a href="#" aria-label="Facebook"><FaFacebook /></a>
            <a href="#" aria-label="Instagram"><FaInstagram /></a>
            <a href="#" aria-label="TikTok"><FaTiktok /></a>
            <a href="#" aria-label="Twitter"><FaTwitter /></a>
          </SocialLinks>
        </Column>
        <Column>
          <h3>CONNECT</h3>
          <p>+1234567890</p>
          <p>varnixx9@gmail.com</p>
        </Column>
        <Column>
          <h3>INSPIRE</h3>
          <Input type="email" placeholder="Enter your email address here" />
          <Button>Submit your request now</Button>
        </Column>
      </FooterContent>
      <Copyright>
        © 2025. All rights reserved.
      </Copyright>
    </FooterContainer>
  );
};

export default FooterSection;