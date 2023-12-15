import { SignUp } from "../components/SignUp";
import { Banner } from "../components/Banner";
import { Fragment } from "react";

export function Sign() {
  return (
    <Fragment>
      <Banner Url="../../Imgs/Sliders/SignIn.jpg" Message="Sign Up" />
      <SignUp />
    </Fragment>
  );
}
