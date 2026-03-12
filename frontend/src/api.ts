import axios from "axios";

const api = axios.create({
  baseURL: "/api",
});

export interface Post {
  id: number;
  user_id: number;
  title: string;
  text: string;
  created_at: string;
  updated_at: string;
}

export async function fetchUserPosts(
  userId: number,
  limit: number,
  offset: number,
): Promise<Post[]> {
  const response = await api.get<Post[]>(`/posts/user/${userId}`, {
    params: { limit, offset },
  });
  return response.data;
}

export async function fetchPost(postId: number): Promise<Post> {
  const response = await api.get<Post>(`/posts/${postId}`);
  return response.data;
}

