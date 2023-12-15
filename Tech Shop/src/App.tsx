import { Routes, Route } from "react-router-dom";
import { Container } from "react-bootstrap";
import { Fragment } from "react";
import { Navbar } from "./components/Navbar";
import { Footer } from "./components/Footer";
import { Home } from "./pages/Home";
import { Store } from "./pages/Store";
import { AboutUs } from "./pages/AboutUs";
import { Cart } from "./pages/Cart";
import { Sign } from "./pages/Sign";
import { Login } from "./pages/Login";

function App() {
  return (
    <Fragment>
      <Navbar />
      <Container fluid className="p-0">
        <Routes>
          <Route path="/" element={<Home />}></Route>
          <Route path="/Store" element={<Store />}></Route>
          <Route path="/AboutUs" element={<AboutUs />}></Route>
          <Route path="/Cart" element={<Cart />}></Route>
          <Route path="/Sign" element={<Sign />}></Route>
          <Route path="/Login" element={<Login />}></Route>
        </Routes>
      </Container>
      <Footer />
    </Fragment>
  );
}

export default App;
