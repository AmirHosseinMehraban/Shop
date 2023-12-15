import { Col, Container, Row } from "react-bootstrap";
import { ZodType, z } from "zod";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { MdPerson } from "react-icons/md";
import { FaUserFriends } from "react-icons/fa";
import { FaPhone } from "react-icons/fa6";
import { BsFillEnvelopeAtFill } from "react-icons/bs";
import { BsFillCalendarDateFill } from "react-icons/bs";
import { RiLock2Fill } from "react-icons/ri";

type SignUpProps = {
  Name: string;
  UserName: string;
  Phone: string;
  email: string;
  Age: string;
  password: string;
  confirmPassword: string;
};

export function SignUp() {
  // error handeling with zod

  const Schema: ZodType<SignUpProps> = z
    .object({
      Name: z
        .string()
        .min(3, { message: " Name must be at least 3 characters " })
        .max(30, { message: " Name must contain at most 30 characters " }),
      UserName: z
        .string()
        .min(3, { message: " UserName must be at least 3 characters " })
        .max(30, { message: " UserName must contain at most 30 characters " }),
      Phone: z
        .string()
        .min(6, { message: " Phone number must be at least 6 digits" })
        .max(12, { message: " Phone number must contain at most 12 digits" })
        .refine((val) => !Number.isNaN(val), {
          message: "Phone number contain only digits",
        }),
      email: z.string().email(),
      Age: z
        .string(),
        
      password: z
        .string()
        .min(8, { message: "Password must be at least 8 characters" })
        .max(30, { message: "Password must contain at most 30 characters" }),
      confirmPassword: z
        .string()
        .min(8, { message: "Password must be at least 8 characters" })
        .max(30, { message: "Password must contain at most 30 characters" }),
    })

    .refine((data) => data.password === data.confirmPassword, {
      message: "Passwords do not match",
      path: ["confirmPassword"],
    });

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<SignUpProps>({
    resolver: zodResolver(Schema),
  });

  const submitData = (data: SignUpProps) => {
    console.log("Done", data);
  };

  return (
    <Container>
      <Row className="justify-content-center">
        <Col md={6} sm={12}>
          <form className="Sign-up" onSubmit={handleSubmit(submitData)}>
            <h2>Sign Up</h2>

            <MdPerson />
            <label htmlFor="Name" className="form-label">
              Name
            </label>
            <input
              id="Name"
              className="form-control"
              type="text"
              {...register("Name")}
            />
            {errors.Name && <span>{errors.Name.message}</span>}

            <FaUserFriends />
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

            <FaPhone />
            <label htmlFor="Phone" className="form-label">
              Phone
            </label>
            <input
              id="Phone"
              className="form-control"
              type="number"
              {...register("Phone")}
            />
            {errors.Phone && <span>{errors.Phone.message}</span>}

            <BsFillEnvelopeAtFill />
            <label htmlFor="Email" className="form-label">
              Email
            </label>
            <input
              id="Email"
              className="form-control"
              type="email"
              {...register("email")}
            />
            {errors.email && <span>{errors.email.message}</span>}

            <BsFillCalendarDateFill />
            <label htmlFor="Age" className="form-label">
              BirthDay
            </label>
            <input
              id="Age"
              className="form-control"
              type="date"
              {...register("Age")}
            />
            {errors.Age && <span>{errors.Age.message}</span>}

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

            <RiLock2Fill />
            <label htmlFor="Confirm-Password" className="form-label">
              Confirm Password
            </label>
            <input
              id="Confirm-Password"
              className="form-control"
              type="Password"
              {...register("confirmPassword")}
            />
            {errors.confirmPassword && (
              <span>{errors.confirmPassword.message}</span>
            )}
            <button className="btn" type="submit">
              Sign Up
            </button>
          </form>
        </Col>
      </Row>
    </Container>
  );
}
