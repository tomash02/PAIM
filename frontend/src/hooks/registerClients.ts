import axios from "axios";

interface Client {
  email: string;
  payment_address: string;
  delivery_address: string;
  nip: string;
  orders: string;
  password: string;
  company_name: string;
}

const registerClients = () => {
  const addClient = async (clientData: Client): Promise<void> => {
    try {
      const response = await axios.post("http://localhost:8000/api/register", clientData);
      console.log("Client registered successfully:", response.data);
    } catch (error) {
      console.error("Failed to register client:", error);
      throw new Error("Could not register client");
    }
  };

  return { addClient };
};

export default registerClients;