import { Fragment } from "react";
import { Container} from "react-bootstrap";
import Carousel from "react-bootstrap/Carousel";

export function Home() {
  return (
    <Fragment>
      <Container fluid className="Slider p-0">
        <Carousel fade>
          <Carousel.Item>
            <img
              src="../../Imgs/Sliders/HomePageSlider01.jpeg"
              alt="pic"
            />
            <Carousel.Caption>
              <h1>
                <strong>Tech</strong> Shop
              </h1>
              <h5>Level Up With Tech Shop</h5>
            </Carousel.Caption>
          </Carousel.Item>
          <Carousel.Item>
            <img
              src="../../Imgs/Sliders/HomePageSlider02.jpeg"
              alt="pic"
            />
            <Carousel.Caption>
              <h1>Tech Shop</h1>
              <h5>have great time with tech shop</h5>
              <h5> reliable , organized & satisfaction</h5>
              <h5>all at once</h5>
            </Carousel.Caption>
          </Carousel.Item>
        </Carousel>
      </Container>
    </Fragment>
  );
}
