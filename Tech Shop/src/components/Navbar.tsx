import { Container, Row, Col } from "react-bootstrap";
import { Nav, Navbar as NavbarBs } from "react-bootstrap";
import { Button } from "react-bootstrap";
import { NavLink } from "react-router-dom";
import { CgShoppingCart } from "react-icons/cg";
import { GiEternalLove } from "react-icons/gi";
import { RiLoginBoxLine } from "react-icons/ri";
import "../assets/Css/Style.css";

export function Navbar() {
  return (
    <NavbarBs expand="lg" className="Navbar" sticky="top">
      <Container>
        <Row>
          <Col md={1} xs={3}>
            <div className="Logo">
              <img src="../../public/Imgs/Logo.png" alt="pic" />
            </div>
          </Col>
          <Col md={9} xs={5}>
            <NavbarBs.Toggle aria-controls="basic-navbar-nav" />
            <NavbarBs.Collapse id="basic-navbar-nav">
              <Nav>
                <Nav.Link to="/" as={NavLink}>
                  Home
                </Nav.Link>
                <Nav.Link to="/AboutUs" as={NavLink}>
                  About Us
                </Nav.Link>
                <Nav.Link to="/Store" as={NavLink}>
                  Store
                </Nav.Link>
                <Nav.Link to="/Cart" as={NavLink}>
                  Cart
                </Nav.Link>
              </Nav>
            </NavbarBs.Collapse>
          </Col>
          <Col md={2} xs={4}>
            <div className="nav-action">
              <Button  className="Shop-cart-list">
                <CgShoppingCart />
                <div className="Number Shop-cart-list-number">
                  0
                </div>
              </Button>
              <Button className="Shop-cart-favorite">
                <GiEternalLove />
                <div className="Number Shop-cart-favorite-number">0</div>
              </Button>
              <a href="/Login">
                <Button className="Shop-cart-favorite">
                  <RiLoginBoxLine />
                </Button>
              </a>
            </div>
          </Col>
        </Row>
      </Container>
    </NavbarBs>
  );
}
