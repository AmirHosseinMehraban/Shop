import { Banner } from "../components/Banner";
import { Fragment } from "react";
import { Col, Container, Row } from "react-bootstrap";
import { ZodType, z } from "zod";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { BsPersonCircle } from "react-icons/bs";
import { IoPerson } from "react-icons/io5";
import { RiLock2Fill } from "react-icons/ri";

type LoginProps = {
  UserName: string;
  password: string;
  Remember: boolean;
};

export function Login() {
  const Schema: ZodType<LoginProps> = z.object({
    UserName: z
      .string()
      .min(3, { message: " UserName must be at least 3 characters " })
      .max(30, { message: " UserName must contain at most 30 characters " }),
    password: z
      .string()
      .min(8, { message: "Password must be at least 8 characters" })
      .max(30, { message: "Password must contain at most 30 characters" }),
    Remember: z.boolean(),
  });

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<LoginProps>({
    resolver: zodResolver(Schema),
  });

  const submitData = (data: LoginProps) => {
    console.log("Done", data);
  };
  return (
    <Fragment>
      <Banner Url="../../Imgs/Sliders/LoginBanner.jpg" Message="Login" />
      <Container>
        <Row className="justify-content-center">
          <Col md={5} sm={12} className="p-0">
            <div className="login-image">
              <img src="../../Imgs/Login.jpg" alt="pic" />
            </div>
          </Col>
          <Col md={5} sm={12} className="p-0">
            <form className="Sign-up Login" onSubmit={handleSubmit(submitData)}>
              <div className="Login-icon">
                <BsPersonCircle />
              </div>
              
              <IoPerson />
              <label htmlFor="UserName" className="form-label">
                User Name
              </label>
              <input
                id="UserName"
                className="form-control"
                type="text"
                {...register("UserName")}
              />
              {errors.UserName && <span>{errors.UserName.message}</span>}
              
              <RiLock2Fill />
              <label htmlFor="Password" className="form-label">
                Password
              </label>
              <input
                id="Password"
                className="form-control"
                type="Password"
                {...register("password")}
              />
              {errors.password && <span>{errors.password.message}</span>}

              <input
                id="Remember"
                className="Remember"
                value="Remember"
                type="checkbox"
                {...register("Remember")}
              />
              <label htmlFor="Remember" className="form-label remember">
                Remember me
              </label>
              <a className="Forgat-password" href="#">
                Forgot Password ?
              </a>
              <button className="btn" type="submit">
                Login
              </button>
              <a className="account" href="/Sign">
                Don't have an account yet ? Sign Up
              </a>
            </form>
          </Col>
        </Row>
      </Container>
    </Fragment>
  );
}
