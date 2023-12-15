import { Col, Container, Row } from "react-bootstrap";
import { MdKeyboardDoubleArrowRight } from "react-icons/md";
import { FaPhoneVolume } from "react-icons/fa6";
import { BsEnvelopeAtFill } from "react-icons/bs";
import { FaWhatsapp, FaInstagram } from "react-icons/fa";
import { FaXTwitter } from "react-icons/fa6";
import { FaLinkedinIn } from "react-icons/fa6";

export function Footer() {
  return (
    <Container fluid className="Footer p-0">
      <Row className="justify-content-center">
        <Col md={3} xs={12}>
          <div className="footer-address">
            <div className="logo-footer">
              <img src="../../public/Imgs/Logo.png" alt="pic" />
            </div>
            <p>
              At <strong>Tech Shop</strong> , we're more than just a computer equipment store
              we're your technology partners.
            </p>
          </div>
        </Col>
        <Col md={1} xs={12} />
        <Col md={3} xs={12}>
          <div className="footer-links">
            <h5><strong>Useful</strong> Links</h5>
            <ul>
              <li>
                <MdKeyboardDoubleArrowRight />
                <a href="#">Home</a>
              </li>
              <li>
                <MdKeyboardDoubleArrowRight />
                <a href="#">About Us</a>
              </li>
              <li>
                <MdKeyboardDoubleArrowRight />
                <a href="#">Contact Us</a>
              </li>
              <li>
                <MdKeyboardDoubleArrowRight />
                <a href="#">Product</a>
              </li>
            </ul>
          </div>
        </Col>
        <Col md={3} xs={12}>
          <div className="footer-contact">
            <h5><strong> Contact </strong>info</h5>
            <ul>
              <li>
                <FaPhoneVolume />
                <a href="tel:+982177123456">021-77123456</a>
              </li>
              <li>
                <FaPhoneVolume />
                <a href="tel:+982177123456">021-77123456</a>
              </li>
              <li>
                <BsEnvelopeAtFill />
                <a href="mailto:example@support.com">example@support.com</a>
              </li>
            </ul>
            <ul className="sm-list">
              <li>
                <a href="#" target="_blank">
                  <FaWhatsapp />
                </a>
              </li>
              <li>
                <a href="#" target="_blank">
                  <FaXTwitter />
                </a>
              </li>
              <li>
                <a href="#" target="_blank">
                  <FaInstagram />
                </a>
              </li>
              <li>
                <a href="#" target="_blank">
                  <FaLinkedinIn />
                </a>
              </li>
            </ul>
          </div>
        </Col>
      </Row>
    </Container>
  );
}
