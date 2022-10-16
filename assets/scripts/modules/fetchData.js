export default async function fetchData(url) {
  try {
    const response = await fetch(url);

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    return await response.json();
  } catch (e) {
    // eslint-disable-next-line no-console
    console.error(e);
  }

  return true;
}
