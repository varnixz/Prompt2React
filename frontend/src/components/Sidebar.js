import React from 'react';
import styled from 'styled-components';
import { Link } from 'react-scroll';
import { AiOutlineHome, AiOutlineCompass, AiOutlineFire, AiOutlineInfoCircle, AiOutlineMenu, AiOutlineClose } from 'react-icons/ai';
import prof from "../assets/prof.jpeg";

const SidebarContent = styled.nav`
  position: fixed;
  top: 0;
  left: 0;
  width: 200px;
  height: 100vh;
  background:  #6B5B6E;
  color: white;
  transform: translateX(${props => props.isOpen ? '0' : '-100%'});
  transition: transform 0.3s ease-in-out;
  z-index: 999;
`;

const ProfileSection = styled.div`
  padding: 20px;
  text-align: center;
  margin-bottom: 20px;

  img {
    width: 80px;
    height: 80px;
    border-radius: 50%;
    margin-bottom: 10px;
    border: 3px solid rgba(255, 255, 255, 0.2);
  }

  h3 {
    color: white;
    font-size: 1.2rem;
    margin: 10px 0;
  }
`;

const MenuItem = styled(Link)`
  display: flex;
  align-items: center;
  padding: 12px 20px;
  cursor: pointer;
  transition: all 0.3s ease;
  color: rgba(255, 255, 255, 0.9);
  text-decoration: none;
  margin: 5px 0;

  &:hover {
    background: rgba(255, 255, 255, 0.1);
    color: white;
  }

  svg {
    font-size: 20px;
    margin-right: 12px;
    color: rgba(255, 255, 255, 0.9);
  }
`;

const SidebarContainer = styled.div`
  position: fixed;
  top: 20px;
  left: 20px;
  z-index: 1000;
`;

const ToggleButton = styled.button`
  background: transparent;
  border: none;
  border-radius: 50%;
  width: 45px;
  height: 45px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s ease;

  &:hover {
    transform: scale(1.05);
  }

  svg {
    color:  #5A4768;
    font-size: 24px;
  }
`;

const MenuItems = styled.div`
  padding-top: 20px;
`;

const Overlay = styled.div`
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(139, 114, 142, 0.3);
  opacity: ${props => props.isOpen ? 1 : 0};
  visibility: ${props => props.isOpen ? 'visible' : 'hidden'};
  transition: all 0.3s ease;
  z-index: 998;
  pointer-events: ${props => props.isOpen ? 'auto' : 'none'};
`;

const CloseButton = styled.button`
  position: absolute;
  top: 20px;
  right: 20px;
  background: none;
  border: none;
  color: rgba(255, 255, 255, 0.9);
  font-size: 24px;
  cursor: pointer;

  &:hover {
    color: white;
  }
`;

const Sidebar = ({ isOpen, setIsOpen }) => {
  const closeSidebar = () => {
    setIsOpen(false);
  };

  return (
    <>
      <SidebarContainer>
        <ToggleButton onClick={() => setIsOpen(true)}>
          <AiOutlineMenu />
        </ToggleButton>
      </SidebarContainer>

      <SidebarContent isOpen={isOpen}>
        <ProfileSection>
          <img src={prof} alt="Profile" />
          <h3>Karan and Shubham</h3>
        </ProfileSection>
        <MenuItems>
          <MenuItem to="dashboard" smooth={true} duration={500} onClick={closeSidebar}>
            <AiOutlineHome />
            <span>Dashboard</span>
          </MenuItem>
          <MenuItem to="components" smooth={true} duration={500} onClick={closeSidebar}>
            <AiOutlineCompass />
            <span>Components</span>
          </MenuItem>
          <MenuItem to="tables" smooth={true} duration={500} onClick={closeSidebar}>
            <AiOutlineFire />
            <span>Tables</span>
          </MenuItem>
          <MenuItem to="forms" smooth={true} duration={500} onClick={closeSidebar}>
            <AiOutlineInfoCircle />
            <span>Forms</span>
          </MenuItem>
          <MenuItem to="about" smooth={true} duration={500} onClick={closeSidebar}>
            <AiOutlineInfoCircle />
            <span>About</span>
          </MenuItem>
        </MenuItems>
      </SidebarContent>

      <Overlay isOpen={isOpen} onClick={closeSidebar} />
    </>
  );
};

export default Sidebar;