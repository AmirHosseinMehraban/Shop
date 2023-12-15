import { Container } from "react-bootstrap";

type BannerProps = {
  Url: string;
  Message: string;
};

export function Banner({ Url, Message }: BannerProps) {
  return (
    <Container fluid className="Banner p-0">
      <img src={Url} alt={Message} />
      <div className="Massage-banner">
        <h1>{Message}</h1>
      </div>
    </Container>
  );
}
